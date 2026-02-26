from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book
BOOKS = [
    {
        "slug": "otkan-kunlar",
        "title": "Abdulla Qodiriy — O‘tkan kunlar",
        "desc": "Jamiyat, qadriyatlar va muhabbat mavzularini tarixiy muhitda juda ta’sirli yoritadi.",
        "tags": ["Badiiy", "O‘zbek adabiyoti"]
    },
    {
        "slug": "kichkina-shahzoda",
        "title": "Antoine de Saint-Exupéry — Kichkina shahzoda",
        "desc": "Do‘stlik, mas’uliyat va qalb bilan ko‘rish haqida sodda, lekin chuqur asar.",
        "tags": ["Falsafa", "Badiiy"]
    },
    {
        "slug": "atomic-habits",
        "title": "James Clear — Atomic Habits",
        "desc": "Kichik odatlar orqali katta natija: tizim, intizom va odatlarni qurish bo‘yicha amaliy yo‘l.",
        "tags": ["Motivatsiya", "O‘zini rivojlantirish"]
    },
    {
        "slug": "clean-code",
        "title": "Robert C. Martin — Clean Code",
        "desc": "Kod yozish madaniyati: o‘qiladigan, toza va qo‘llab-quvvatlanadigan kod tamoyillari.",
        "tags": ["IT", "Dasturlash"]
    },
    {
        "slug": "deep-work",
        "title": "Cal Newport — Deep Work",
        "desc": "Diqqatni jamlash va samarali ishlash: chalg‘ituvchilarsiz chuqur mehnat uslubi.",
        "tags": ["Samaradorlik", "O‘qish"]
    },
    {
        "slug": "1984",
        "title": "George Orwell — 1984",
        "desc": "Nazorat kuchaygan jamiyatda erkinlik va haqiqatning yo‘qolishi haqida ogohlantiruvchi asar.",
        "tags": ["Badiiy", "Distopiya"]
    },
]

def home(request):
    books = Book.objects.order_by("-created_at")
    return render(request, "katalog/home.html", {
        "student_fullname": "FAMILIYA ISM",
        "books": books
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "katalog/book_detail.html", {
        "student_fullname": "FAMILIYA ISM",
        "book": book
    })