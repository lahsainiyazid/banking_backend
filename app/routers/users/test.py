from user_classes import update_user 


update=update_user(email="lahsainitv@gmail.com",user_id=10)
cols=[]
values=[]
data=update.model_dump(exclude_unset=True)
for key,value in data.items():
    cols.append(f"{key}=%s")
    values.append(value)
    print(f"{key}:{value}")
set_query=','.join(cols)
print(set_query)
