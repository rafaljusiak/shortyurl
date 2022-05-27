#!/usr/bin/env python3

import logging
import os
import time
import psycopg2

logger = logging.getLogger()

while True:
    try:
        logger.warning("Checking connection with PostgreSQL...")
        psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )
    except psycopg2.OperationalError:
        logger.warning("Cannot connect to PostgreSQL")
        logger.error("Sleeping for 1 second")
        time.sleep(1)
    else:
        logger.warning("PostgreSQL is available!")
        break
