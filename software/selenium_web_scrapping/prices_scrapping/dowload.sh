{
  python -m venv scrapper
  source ./scrapper/bin/activate
  pip install -r ./requirement.txt
} || {
  echo "Un error ha ocurrido en la creacion del ambiente de trabajo, intente nuevamente"
}

{
  wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux-aarch64.tar.gz
  tar -zxf geckodriver-v0.34.0-linux-aarch64.tar.gz
  mv ./geckodriver ./scrapper/bin/
  rm ./geckodriver-v0.34.0-linux-aarch64.tar.gz
} || {
  echo "Un error ha ocurrido en la instalacion del driver para selenium, intente nuevamente"
}
