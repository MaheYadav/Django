from django.shortcuts import render

d2 = {
    "101": {"name": "Ravi", "exp": 2.5, "sal": 125000.00, "ts": ["C", "C++", "Java", "Python"]},
    "102": {"name": "Kumar", "exp": 5, "sal": 185000.00,
            "ts": ["C", "C++", "Core Java", "Advance Java", "spring", "Python", "Django", "Flask", "HTML", "CSS",
                   "JavaScript", "Bootstrap", "Angular JS"]},
    "103": {"name": "Mohan", "exp": 1.2, "sal": 275000.00,
            "ts": ["C", "Core Java", "Python", "Django", "HTML", "CSS", "JavaScript", "Angular JS"]},
    "104": {"name": "Anil", "exp": 2.0, "sal": 135000.00,
            "ts": ["C", "Core Java", "Python", "HTML", "CSS", "JavaScript"]},
    "105": {"name": "Guna", "exp": 3.5, "sal": 145000.00, "ts": ["Core Java", "Python", "HTML", "CSS"]},
    "106": {"name": "Prashanth", "exp": 7, "sal": 155000.00,
            "ts": ["Core Java", "Advance Java", "spring", "JavaScript", "Bootstrap"]},
    "107": {"name": "Madhu", "exp": 5.8, "sal": 165000.00,
            "ts": ["C", "C++", "Python", "Django", "Bootstrap", "Angular JS"]},
    "108": {"name": "Hemanth", "exp": 0.5, "sal": 175000.00, "ts": ["C", "C++"]},
    "109": {"name": "Sai Krishna", "exp": 3, "sal": 195000.00, "ts": ["HTML", "CSS", "JavaScript", "Angular JS"]},
    "110": {"name": "Kunal", "exp": 4.5, "sal": 225000.00, "ts": ["Python", "Flask", "HTML"]}
}
d1 = {
    "101":{"name":"Ravi","exp":2.5,"sal":125000.00},
    "102":{"name":"Kumar","exp":5,"sal":185000.00},
    "103":{"name":"Mohan","exp":1.2,"sal":275000.00},
    "104":{"name":"Anil","exp":2.0,"sal":135000.00},
    "105":{"name":"Guna","exp":3.5,"sal":145000.00},
    "106":{"name":"Prashanth","exp":7,"sal":155000.00},
    "107":{"name":"Madhu","exp":5.8,"sal":165000.00},
    "108":{"name":"Hemanth","exp":0.5,"sal":175000.00},
    "109":{"name":"Sai Krishna","exp":3,"sal":195000.00},
    "110":{"name":"Kunal","exp":4.5,"sal":225000.00}
     }


def showIndex(request):
    return render(request,"index.html",{"data":d1})


def showIndex1(request):
    return render(request,"index1.html",{"data":d1})


def showIndex2(request):
    return render(request,"index2.html",{"data":d1})
