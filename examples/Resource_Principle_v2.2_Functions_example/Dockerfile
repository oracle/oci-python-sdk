FROM fnproject/python:3.6-dev as build-stage
WORKDIR /function
ADD . /function/
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
        rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv
RUN rm -fr /function/.pip_cache


FROM fnproject/python:3.6
WORKDIR /function
COPY --from=build-stage /function /function
COPY --from=build-stage /python /python
RUN chmod -R o+r /python /function
# Usually, users don't need to install python sdk here, but directly add oci in requirement.txt
ENV PYTHONPATH=/function:/python
RUN pip3 install oci-2.17.1+preview.1-py2.py3-none-any.whl
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]