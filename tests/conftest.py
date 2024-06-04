import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession.builder \
        .appName("PySpark Test") \
        .master("local[2]") \
        .getOrCreate()
    yield spark
    spark.stop()