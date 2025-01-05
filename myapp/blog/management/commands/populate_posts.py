from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="this command is inserts post data"


    def handle(self, *args: Any, **options: Any) -> str | None:

        Post.objects.all().delete()

        titles=[
    "Life Between the Fields and Dreams", 
    "Conversations Under the Moonlight",
    "A Day in the Life of a Modern Farmer", 
    "Tea, Reels, and Family Bonds", 
    "The Niece Who Brightens My World",
    "From Farm to Fortune: A Journey of Perseverance", 
    "Interview Prep Chronicles",
    "Dream Big, Work Hard",
    "Balancing Rural Roots and Urban Ambitions",
    "Every Day Counts: The Road to Success", 
    "Vlogs That Inspire Laughter", 
    "Late-Night Chats and Endless Stories",
    "Farming in the Day, Dreams at Night", 
    "Reels, Tea, and a Slice of Life",
    "Finding Joy in Simple Pleasures",
    "The Bond of a Brother, The Love of a Son", 
    "Daily Talks with My Special Someone",
    "Moments That Matter with My Sister's Daughter",
    "Heart-to-Heart Across the Miles", 
    "In the Company of Loved Ones"
]

        content=[
    

"Exploring the balance between work, family, and personal dreams, where every day holds new opportunities and challenges.",

"Late-night chats filled with laughter and deep thoughts, reflecting on life and sharing dreams under the stars.",

"A glimpse into the daily routines of farming, where hard work and dedication shape the land and the future.",

"Starting the day with a cup of tea and a scroll through fun reels, finding small moments of joy before diving into daily tasks.",

"Spending time with a niece who brings pure happiness, creating memories that last a lifetime.",

"An inspiring journey of growth, resilience, and ambition, as one navigates through challenges on the way to success.",

"Preparing for job interviews with determination and focus, learning new skills and gaining confidence for the next big opportunity.",

"Chasing dreams with unwavering belief, pushing past obstacles, and giving everything to achieve what’s possible.",

"Finding a way to stay rooted in one’s origins while pursuing modern ambitions, blending the best of both worlds.",

"Embracing the idea that every small step counts, pushing forward every day toward bigger goals and dreams.",

"Sharing moments of joy and laughter from vlogs that spark inspiration, creating a sense of connection and positivity.",

"Staying up late, swapping stories, and cherishing the quiet moments that make life so memorable.",

"From sunrise to sunset, working in the fields, and at night letting dreams take over—finding peace in both.",

"Enjoying simple pleasures like watching funny reels and sipping tea, allowing life’s small joys to shape the day.",

"Learning to appreciate the beauty of life’s simple moments—family, laughter, and quiet reflection.",

"The strong bond between siblings, where love and support grow over the years, creating a foundation of trust and care.",

"Connecting with a special person every day, sharing everything from trivial thoughts to heartfelt feelings.",

"Watching a young child grow and create memories, relishing the small moments of innocence and wonder.",

"Having meaningful, long-distance conversations, staying close despite the distance, and sharing everything with a loved one.",

"Surrounding yourself with loved ones who lift you up, ensuring you’re never alone in life’s journey."
]

        img_urls=[
 
    "https://picsum.photos/id/1/800/400" ,   
    "https://picsum.photos/id/2/800/400" ,  
    "https://picsum.photos/id/3/800/400" ,   
    "https://picsum.photos/id/4/800/400" ,   
    "https://picsum.photos/id/5/800/400" ,   
    "https://picsum.photos/id/6/800/400" ,   
    "https://picsum.photos/id/7/800/400" ,   
    "https://picsum.photos/id/8/800/400" ,   
    "https://picsum.photos/id/9/800/400" ,   
    "https://picsum.photos/id/10/800/400",    
    "https://picsum.photos/id/11/800/400",    
    "https://picsum.photos/id/12/800/400",    
    "https://picsum.photos/id/13/800/400",    
    "https://picsum.photos/id/14/800/400",    
    "https://picsum.photos/id/15/800/400",    
    "https://picsum.photos/id/16/800/400",    
    "https://picsum.photos/id/17/800/400",    
    "https://picsum.photos/id/18/800/400",    
    "https://picsum.photos/id/19/800/400",    
    "https://picsum.photos/id/20/800/400"    
    
]

        for title,content,img_url in zip(titles,content,img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))