FROM python:3.12-slim
WORKDIR /usr/local/app

COPY ./requirements.txt ./setup.sh ./

RUN chmod +x ./setup.sh
RUN ./setup.sh

COPY src ./src
EXPOSE 8000

USER root
CMD ["uv", "run", "python", "-m", "src.main"]
