from django.shortcuts import render
from main.models import Vote, Community
from django.db.models import Count

'''
Index View: Main Results Page

url: /results

# TODO Corey | Add Documentation
'''

def index(response):

    top_communities = Vote.objects.all().values('community_key').annotate(total=Count('community_key')).order_by('-total')[:10]
   
    community_data = []
    for communities in top_communities:
        code = communities.get("community_key")
        community_data.append(Community.objects.all().filter(id=code).values('code'))

    final_community_data = []
    for community in community_data:
        final_community_data.append(community[0].get('code'))
        
    print("----------")
    print(top_communities)        
    print("----------")
    print(community_data)
    print("----------")
    print(final_community_data)

    ctx = {"community_codes":final_community_data}
    return render(response, "results/results.html", ctx)