#!/bin/bash

celery -A tasks.celery_ worker --loglevel=info
