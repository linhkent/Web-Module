import mlab
from food import Food

mlab.connect()

# f = Food(title = "Bánh cuốn", link = "https://www.google.com/imgres?imgurl=http://lambanh365.com/wp-content/uploads/2015/04/C%25C3%25A1ch-l%25C3%25A0m-b%25C3%25A1nh-cu%25E1%25BB%2591n-b%25E1%25BA%25B1ng-n%25E1%25BB%2593i-h%25C6%25A1i-th%25C6%25A1m-ngon-11.jpg&imgrefurl=http://lambanh365.com/cach-lam/cach-lam-banh-cuon-bang-noi-hoi-thom-ngon/&h=368&w=550&tbnid=ZgNb5BSlnmS2JM:&q=B%C3%A1nh+cu%E1%BB%91n&tbnh=133&tbnw=200&usg=AI4_-kQu34H8oLrTuhJlMmwNdm6s6KIw8Q&vet=12ahUKEwj1wJya1o3gAhVHMd4KHebmAuoQ_B0wE3oECAsQCQ..i&docid=9OsEBvrVjc2G9M&itg=1&client=firefox-b-ab&sa=X&ved=2ahUKEwj1wJya1o3gAhVHMd4KHebmAuoQ_B0wE3oECAsQCQ")
# f.save()

f_objects = Food.objects()
# f_first = f_objects[0]
# print(f_first.title)
# print(f_first.link)

# print(len(f_objects))
# print(f_objects.count())
# for f in f_objects:
#     print (f)

# f = f_objects[1]
# # f.update(set__title = 'Bún chả', set__link = 'Ếu có link')
# # f.reload()
# # print(f.title)
# f.delete()

f = f_objects.with_id("5c4d7d45697dae30c83fb617")
if f != None:
    f.delete()
    print('Ok')
else:
    print('Not found')