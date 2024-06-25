#!/usr/bin/env python
# coding: utf-8

# ### ipywidgets

# In[1]:


import ipywidgets as widgets

print(widgets.__version__)


# In[2]:


from ipywidgets import interact,interactive,interact_manual,interactive_output,fixed


# ## 1.interact()
# The interact function ( ipywidgets. interact ) automatically creates user interface (UI) controls for exploring code and data interactively.

# In[7]:


#simple UI creation
def square(x):
    return x*x
interact(square,x=5);


# In[6]:


def square(x=5):
    return x*x
interact(square);


# In[8]:


def square(x):
    return x*x
interact(square,x=5)# if we miss the semicolumn at this line it shows the <function__main__.square(x)>


# In[9]:


@interact
def square(x=5):
    return x*x


# In[10]:


def formula(a,b,c):
    return a*5+b*2+c*1


# In[15]:


widgets.interact(formula,a=2,b=2,c=1)


# In[16]:


#fix value of argument
interact(formula,a=1,b=2,c=fixed(10))


# ### how interact() determines widget type

# In[19]:


interact(formula,a=(1,10),b=(1,15),c=fixed(10))


# In[20]:


interact(formula,a=(1.0,10),b=(1,15),c=fixed(10))


# In[21]:


interact(formula,a=(1,10,2),b=(1,15,3),c=fixed(10)) #a=(min,max,step)


# In[22]:


def concate(a,b):
    return a+" "+b


# In[25]:


interact(concate,a="hello",b="world");


# In[26]:


interact(concate,a=["hello","hi","welcome to"],b=["world","friends","keats"]);


# ### create widget objects for more flexibility

# In[32]:


w1=widgets.IntSlider(value=2,min=0,max=10,step=1,description="hello")
w2=widgets.IntSlider(value=2,min=0,max=10,step=1,description="hello hi")
interact(formula,a=w1,b=w2,c=fixed(10));


# In[33]:


w1.value, w2.value


# In[34]:


w1.value=4


# In[37]:


str1=widgets.Text(value="hello",description="1st")
str2=widgets.Text(value="world",description="2nd")
interact(concate,a=str1,b=str2);


# In[38]:


str1.value,str2.value


# In[40]:


str1.value="hey"


# In[44]:


drop1=widgets.Dropdown(options=["hello","hi","welcome to"],index=2)
drop2=widgets.Dropdown(options=["world","india","pooja","keats"],index=3)
interact(concate,a=drop1 ,b=drop2);


# In[46]:


drop1.value,drop2.value


# In[48]:


drop1=widgets.Dropdown(options=["hello","hi","welcome to"],index=2)
drop2=widgets.Dropdown(options=["world","india","pooja","keats"],index=3)
interact(concate,a=drop1 ,b=drop2);


# In[52]:


drop1=widgets.Dropdown(options=[("hello",0),("hi",1),("welcome to",2)],index=2)
drop1


# In[54]:


drop1.value


# In[56]:


w=widgets.FloatSlider(value=5.5,min=0,max=10,step=0.5,description="param1")
w


# In[57]:


w.value


# In[59]:


save_model=widgets.Checkbox(description="save model")
save_model


# In[61]:


save_model.value


# In[64]:


radio_buttons=widgets.RadioButtons(options=["option-1","option-2","option-3"],index=2)
radio_buttons


# In[65]:


radio_buttons.value


# ### prevent continuous updates

# In[68]:


w1=widgets.IntSlider(value=2,min=0,max=10,step=1,description="option1")
w2=widgets.IntSlider(value=8,min=0,max=10,step=2,description="option2")
interact(formula,a=w1,b=w2,c=fixed(10));


# In[69]:


w1=widgets.IntSlider(value=2,min=0,max=10,step=1,description="option1",continuous_update=False)
w2=widgets.IntSlider(value=8,min=0,max=10,step=2,description="option1",continuous_update=False)
interact(formula,a=w1,b=w2,c=fixed(10));


# ## 2.interactive() 
# The ipywidgets provides another function called interactive() to create the UI of widgets by passing a function to it.
# Unlike interact() function, interactive() returns objects which does not displays widgets automatically.
# We need to use IPython function display() to display widgets UI as well as the output of a function.

# In[72]:


def h(a,b,c):
    print(a*5+b*7+c*10)
g=interactive(h,a=1,b=2,c=fixed(10));


# In[73]:


display(g)


# In[74]:


type(g)


# In[75]:


g.children


# In[76]:


g.kwargs


# ## 3.interactive_output()
# The interactive_output() function is layout widgets according to our need. 
# The interactive_output() does not generate output UI but it lets us create UI, organize them in a box and pass them to it. 
# This gives us more control over the layout of widgets.

# In[78]:


def h(a,b,c):
    print(a*5+b*7+c*10)
w1=widgets.IntSlider(value=2,min=0,max=20,step=1,description="a")
w2=widgets.IntSlider(value=8,min=0,max=10,step=2,description="b")
g=interactive_output(h,{"a":w1,"b":w2,"c":fixed(10)});
display(w1,w2,g)


# In[79]:


type(g)


# In[80]:


def h(a,b,c):
    print(a*5+b*7+c*10)
w1=widgets.IntSlider(value=2,min=0,max=20,step=1,description="a")
w2=widgets.IntSlider(value=8,min=0,max=10,step=2,description="b")
g=interactive_output(h,{"a":w1,"b":w2,"c":fixed(10)});
display(g,w1,w2)


# In[ ]:




