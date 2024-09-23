from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "cycling",
        "image": "mountains.jpg",
        "author": "Utkarsh Gaikwad",
        "date": date(2024, 9, 23),
        "title": "Cycling from home to Lonavala",
        "excerpt": ("Conquering nearly 100 kilometers, my cycling journey from home to"
                    "Lonavala was a true test of endurance, strength, and passion for"
                    "adventure."),
        "content": ("Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam, nisi. Maxime"
                    "atque praesentium, blanditiis eaque corporis iusto doloremque laboriosam"
                    "assumenda ex harum consequatur, fugiat eos, officiis quae ea voluptates"
                    "neque!\n\n"
                    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam, nisi. Maxime"
                    "atque praesentium, blanditiis eaque corporis iusto doloremque laboriosam"
                    "assumenda ex harum consequatur, fugiat eos, officiis quae ea voluptates"
                    "neque!\n\n"
                    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam, nisi. Maxime"
                    "atque praesentium, blanditiis eaque corporis iusto doloremque laboriosam"
                    "assumenda ex harum consequatur, fugiat eos, officiis quae ea voluptates"
                    "neque!\n\n")
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Utkarsh Gaikwad",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Utkarsh Gaikwad",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post.get("date")


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(
        post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
