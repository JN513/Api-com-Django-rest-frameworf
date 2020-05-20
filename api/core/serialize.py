from rest_framework import serializers


from .models import Usuario

class UsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model =Usuario
        fields =('id','nome','endereço','idade','email','password','username','cpf','perfil','datetime')