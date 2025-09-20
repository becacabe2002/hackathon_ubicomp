#!/bin/bash

docker exec n8n sh -c "n8n import:workflow --input=./config/my_workflow.json"
docker exec n8n sh -c "n8n import:credentials --input=./config/credit.json"
docker exec n8n sh -c "n8n update:workflow --id=123 --active=true"