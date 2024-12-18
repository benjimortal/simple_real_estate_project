from django.forms import ModelForm

from . models import Listing


class ListingForm(ModelForm):
    class Meta:
        # her we must modify witch model we want work with
        model = Listing
        fields =  ['title',
                   'price',
                   'num_bedroom',
                   'num_bathroom',
                   'square_footage',
                   'address',
                   'image']
        
        