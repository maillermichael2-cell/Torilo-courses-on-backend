import webbrowser

user_data = []

print('welcome to json search program developed by McMichaels code')
print("""
        how can i help you today remember you can ask me anything 
""")

user_input = input("Ask me any thing : ")
user_data.append(user_input)

# web search for he user input 
query = f'https://www.google.com/search?q={user_data[0]}'
return_data = webbrowser.open(query)
print(f'Showing the result for your search {user_input} in the browser....')
print('Browser opened with results of your search')
print(return_data)
print(query)
