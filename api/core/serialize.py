from rest_framework import serializers


from .models import Usuario

class UsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model =Usuario
        fields =('id','nome','email','password','username','datetime')