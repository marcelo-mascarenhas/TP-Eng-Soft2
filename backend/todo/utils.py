from .models import Movies
from django.forms.models import model_to_dict



def getMovieDictionary(database_object, title_as_key = True):
    movies = {}
    movies['data'] = {}
    it_num = 0
    
    database_object_iterator = None
    try:
      database_object_iterator = database_object.iterator()
    except Exception as e:
      database_object_iterator = list(database_object)
    
    for star in database_object_iterator:
      target_key = star.title if title_as_key else it_num 
      movies['data'][target_key] = model_to_dict(star)
      it_num += 1
    
    return movies