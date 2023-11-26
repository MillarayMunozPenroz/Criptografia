# Indicar la imágen base
FROM ubuntu:20.10

# Copiar el archivo sources.list en el contenedor en la ruta indicada
COPY sources.list /etc/apt/sources.list

# Evitar que se interactue con el usuario en la instalación
ENV DEBIAN_FRONTED=noninteractive

# Actualizar los paquetes del contenedor && instala el cliente ssh en el contenedor
RUN apt-get update && apt-get install -y sudo net-tools openssh-client
RUN apt-get install -y sudo openssh-server

# Se instala el tshark para las capturas posteriores
RUN apt-get install -y tshark

# Agregar el usuario pedido
RUN useradd -m test
RUN echo 'test:test' | chpasswd

EXPOSE 22


CMD ["bash"]
