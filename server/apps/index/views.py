from datetime import datetime
from time import sleep
import random

from django.shortcuts import render
from django.http import QueryDict


def index(request, rpath=""):
    template = "index.html"

    if rpath != "":
        template = f"slides/{request.path[1:]}.html"

    context = {}

    context["emoji_0"] = random.choice(emojis)
    context["emoji_1"] = random.choice(emojis)
    context["emoji_2"] = random.choice(emojis)
    context["emoji_3"] = random.choice(emojis)
    context["request"] = request
    context["now"] = datetime.now()

    # get get parms
    if request.method == "GET":
        context["get"] = request.GET.items()
    # get post parms
    if request.method == "POST":
        context["post"] = request.POST.items()
    # get put parms
    if request.method == "PUT":
        context["put"] = QueryDict(request.body).items()
    # get delete parms
    if request.method == "DELETE":
        if request.headers.get("Hx-Prompt"):
            context["prompt"] = request.headers.get("Hx-Prompt")
        context["delete"] = QueryDict(request.body).items()

    return render(request, template, context)


def slow(request, rpath=""):
    template = "index.html"

    if rpath != "":
        template = f"slides/{request.path[6:]}.html"

    sleep(6)

    context = {}

    context["emoji_0"] = random.choice(emojis)
    context["emoji_1"] = random.choice(emojis)
    context["emoji_2"] = random.choice(emojis)
    context["emoji_3"] = random.choice(emojis)
    context["request"] = request
    context["now"] = datetime.now()

    # get get parms
    if request.method == "GET":
        context["get"] = request.GET.items()
    # get post parms
    if request.method == "POST":
        context["post"] = request.POST.items()
    # get put parms
    if request.method == "PUT":
        context["put"] = QueryDict(request.body).items()
    # get delete parms
    if request.method == "DELETE":
        context["delete"] = QueryDict(request.body).items()

    return render(request, template, context)


emojis = [
    "🌱",
    "🌲",
    "🌳",
    "🌴",
    "🌵",
    "🌷",
    "🌸",
    "🌹",
    "🌺",
    "🌻",
    "🌼",
    "💐",
    "🌾",
    "🌿",
    "🍀",
    "🍁",
    "🍂",
    "🍃",
    "🍄",
    "🌰",
    "🐀",
    "🐁",
    "🐭",
    "🐹",
    "🐂",
    "🐃",
    "🐄",
    "🐮",
    "🐅",
    "🐆",
    "🐯",
    "🐇",
    "🐰",
    "🐈",
    "🐱",
    "🐎",
    "🐴",
    "🐏",
    "🐑",
    "🐐",
    "🐓",
    "🐔",
    "🐤",
    "🐣",
    "🐥",
    "🐦",
    "🐧",
    "🐘",
    "🐪",
    "🐫",
    "🐗",
    "🐖",
    "🐷",
    "🐽",
    "🐕",
    "🐩",
    "🐶",
    "🐺",
    "🐻",
    "🐨",
    "🐼",
    "🐵",
    "🙈",
    "🙉",
    "🙊",
    "🐒",
]
