from rest_framework import serializers

from .models import Book, Author

    
# class AuthorSerializer(serializers.ModelSerializer):  
#   class Meta:
#     model = Author
#     fields = '__all__'

  
class AuthorSerializer(serializers.Serializer):  
  id = serializers.IntegerField()
  name = serializers.CharField()
  age = serializers.IntegerField()
    
    
class BookSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  price = serializers.IntegerField()
  date = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'])
  author = AuthorSerializer()

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.price = validated_data.get('price', instance.price)
    
    author_data = validated_data.get('author')
    if author_data:
        author_id = author_data.get('id')
        
        if author_id:
            Author.objects.filter(id=author_id).update(id=author_id)
          
            instance.author = Author.objects.get(id=author_id)
        else:
            author, created = Author.objects.get_or_create(name=author_data['name'])
            instance.author = author
    
    instance.save()
    return instance
