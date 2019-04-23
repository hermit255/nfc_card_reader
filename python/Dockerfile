FROM python:2.7
WORKDIR /app
RUN apt-get update \
  && apt-get -y install libusb-1.0-0-dev usbutils\
  && pip install --upgrade pip \
  && pip install nfcpy flask redis requests
CMD ["python", "run.py"]
