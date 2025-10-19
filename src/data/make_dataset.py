# -*- coding: utf-8 -*-
"""
Valida y prepara el dataset para su uso en el proyecto.
- Lee el CSV "crudo" (input_filepath) desde data/raw/
- Realiza chequeos mínimos (shape, columnas esperadas, tipos plausibles)
- Calcula MD5 del archivo de entrada
- Escribe una copia "limpia" en output_filepath (sugerido: data/processed/...)
- Escribe un archivo de metadatos JSON junto a la salida (…_metadata.json)

Uso:
    python -m src.data.make_dataset data/raw/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv \
                                    data/processed/dataset_prestaciones_extrahospitalarias_2025_realista_v1.csv
"""
import click
import logging
import hashlib
import json
from pathlib import Path

import pandas as pd
from dotenv import find_dotenv, load_dotenv

# ---- CONFIG: actualiza si cambian columnas o necesitas ajustar validaciones ----
EXPECTED_COLUMNS = [
    "fecha_solicitud", "edad", "zona", "hospital_origen", "estado_civil", "ocupacion",
    "vivienda_tipo", "ingresos_mensuales", "egresos_mensuales", "grupo_familiar_a_cargo",
    "vehiculos_cantidad", "dni_domicilio_tdf", "disponible_en_red_publica",
    "tiene_cobertura_inicial", "derecho_cobertura_dir", "cud", "informe_social_ok",
    "documentacion_completa", "zona_riesgo_sanitario", "tipo_prestacion", "autorizar"
]

VERSION = "v1.0"
SEED = 2025  # mantené coherente con tu README y data_dictionary


def md5sum(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_columns(df: pd.DataFrame, logger: logging.Logger):
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    extra = [c for c in df.columns if c not in EXPECTED_COLUMNS]
    if missing:
        logger.warning(f"Columnas faltantes: {missing}")
    if extra:
        logger.info(f"Columnas adicionales (no esperadas): {extra}")
    # Reordena si es posible
    present = [c for c in EXPECTED_COLUMNS if c in df.columns]
    df = df[present + [c for c in df.columns if c not in present]]
    return df, missing


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument('output_filepath', type=click.Path(dir_okay=False, path_type=Path))
def main(input_filepath: Path, output_filepath: Path):
    """Convierte datos crudos en un dataset listo para análisis y deja metadatos."""
    logger = logging.getLogger(__name__)
    logger.info(f"Leyendo dataset crudo: {input_filepath}")

    df = pd.read_csv(input_filepath)

    # Chequeos básicos
    logger.info(f"Shape: {df.shape[0]} filas x {df.shape[1]} columnas")
    df, missing = validate_columns(df, logger)

    # Tipos esperados
    soft_expect = {
        "autorizar": "int/bool",
        "fecha_solicitud": "fecha/str",
        "edad": "num",
        "ingresos_mensuales": "num",
        "egresos_mensuales": "num",
        "vehiculos_cantidad": "num",
    }
    for col, exp in soft_expect.items():
        if col in df.columns:
            # si algo luce completamente no numérico donde esperamos num, avisamos
            if exp == "num" and not pd.api.types.is_numeric_dtype(df[col]):
                logger.warning(f"[Tipo sospechoso] '{col}' no parece numérica.")
            if col == "autorizar" and not pd.api.types.is_numeric_dtype(df[col]):
                logger.warning("[Tipo sospechoso] 'autorizar' no es numérica (0/1).")

    # Guarda copia "limpia" (acá no transformamos; solo reordenamos y copiamos)
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_filepath, index=False, encoding="utf-8")
    logger.info(f"Dataset listo guardado en: {output_filepath}")

    # MD5 del archivo de entrada y de salida
    md5_in = md5sum(input_filepath)
    md5_out = md5sum(output_filepath)

    # Metadatos al lado del archivo de salida
    meta_path = output_filepath.with_name(output_filepath.stem + "_metadata.json")
    meta = {
        "version": VERSION,
        "seed": SEED,
        "input_csv": str(input_filepath),
        "output_csv": str(output_filepath),
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "md5_in": md5_in,
        "md5_out": md5_out,
        "expected_columns": EXPECTED_COLUMNS,
        "missing_columns": missing,
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info(f"Metadata escrita en: {meta_path}")
    logger.info(f"MD5 (input):  {md5_in}")
    logger.info(f"MD5 (output): {md5_out}")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]
    load_dotenv(find_dotenv())

    main()
