from app import books,scrape_url
from flask import Flask,render_template,request,url_for,redirect



app=Flask(__name__)

# user_choices={'b':{'name':print_best_books,'descr':'Print the best books!!'},
#               'c':{'name':print_cheap_books,'descr':'Print the cheap books'},
#               'n':{'name':get_next_book,'descr':'Print the next book'}}

user_choices={'b': {'name':'print_best_books','descr':'Print the best books!!'},
              'c':{'name':'print_cheap_books','descr':'Print the cheap books'},
              'n':{'name':'get_next_book','descr':'Print the next book'}}


# def print_best_books():
#     best_books = sorted(books, key = lambda x : x.rating*-1)[0:3]
#     best_books_multipleSort= sorted(books, key= lambda x:(x.rating * -1, x.price))
#     for bb in best_books:
#       print(bb)
      
      
@app.route('/display/<string:my_id>')
def showMethod(my_id):
    if my_id in ('b','c','n'):
         show=user_choices[my_id]
         if(show['name'])=='print_best_books':
             best_books = sorted(books, key = lambda x : x.rating*-1)[:10]
            #  return f'{best_books[0]}'
             return (render_template('books.jinja2',display=best_books[2]))
         elif(show['name'])=='print_cheap_books':
             cheap_books= sorted(books, key= lambda x:(x.rating*-1, x.name))[:10]
            #  return f'{cheap_books[0]}'
             return (render_template('books.jinja2',display=cheap_books[8]))
         elif(show['name'])=='get_next_book':
              next_book=(next((book for book in books )))
            #   return next_book
              return (render_template('books.jinja2',display=next_book))
         else:
           return (render_template('404.jinja2',message='Invalid Input...'))
    


# def print_cheap_books():
#     cheap_books= sorted(books, key= lambda x:(x.rating*-1, x.name))[:10]
#     for cheap_book in cheap_books:
#       print(cheap_book)
       
       
# book_generator=(book for book in books )

# def get_next_book():
#      print(next(book_generator))
    


# def menu():
#     user_input=input(USER_CHOICE)
#     while (user_input!='q'):
#         if user_input in ('b','c','n'):
#             user_choices[user_input]()

# 
# @app.route('/display/form')
# def getUserInput():
#     return render_template('inputForm.jinja2')

    
@app.route('/display/formoutput', methods=['POST','GET'])
def getFormOutput():
     if request.method=='POST':
        # my_id=request.args.get('user')
         my_id=request.form.get('user')
        # print(url_for('showMethod',my_id=my_id))
         return redirect(url_for('showMethod',my_id=my_id))
        # render_template('inputForm.jinja2')
        # return userchoice
     return render_template('inputForm.jinja2')

@app.route('/')
def home():
    
    USER_CHOICE=''' Enter the user Choice:
'b' for best books
'c' for che ap books
'n' for next available books
'q' for quitting
    '''
    user_input=input(USER_CHOICE)
    while (user_input!='q'):
        return ("It is working now!")
       
        #  return (user_choices[user_input]['name'])   
            
if(__name__=='__main__'):
    # app.run(host='127.0.0.1', port = '8080', debug=True)
    # app.run(debug=True)
    app.run(host='0.0.0.0', port = '8080', debug=True)