from django.db import models

# Create your models here.


class Pokemon(models.Model):
    idPokedex = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField()
    generation = models.IntegerField()
    class Meta:
        db_table = 'Pokemon'
    


class PokemonType(models.Model):
    idType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'Type'
        
        
        
class PokemonTypeHasType(models.Model):
    id = models.AutoField(primary_key=True)
    Pokemon_idPokedex = models.ForeignKey(Pokemon,on_delete=models.CASCADE)
    Type_idType = models.ForeignKey(PokemonType,on_delete=models.CASCADE)
    class Meta:
        db_table = 'Pokemon_has_Type'
        
        
        
class TypeVsType(models.Model):
    id = models.AutoField(primary_key=True)
    Attacker = models.ForeignKey(PokemonType,on_delete=models.CASCADE, related_name='type_effectiveness_as_attacker')
    Defender = models.ForeignKey(PokemonType,on_delete=models.CASCADE,related_name='type_effectiveness_as_defender')
    value = models.FloatField()
    class Meta:
        db_table = 'Type_vs_Type'        