import streamlit as st
import time

st.set_page_config(page_title='Nexacore',page_icon='💻')
for key in ['pag','login_password','login_email','reg_name','reg_email','reg_password']:
    if key not in st.session_state:
        st.session_state[key]='login' if key=='page' else ''

if 'page' not in st.session_state:
    st.session_state.page='login'

if'user_name'not in st.session_state:
    st.session_state.user_name=''

if'login_email' not in st.session_state:
    st.session_state.login_email=''

if'login_password' not in st.session_state:
    st.session_state.login_password=''

if st.session_state.page=='login':
    st.title('Welcome to Nexacore')
    st.subheader('ivan app')
    email=st.text_input(label='email',key='login_email',type='email')
    password=st.text_input(label='password',key='login_password',type='password')

    col1,col2,col3=st.columns([1,1,1])
    with col2:
        login=st.button(label='Login',use_container_width=True)
        if login:
            if not st.session_state.login_email.strip() or not st.session_state.login_password.strip():
                st.warning('Please fill in all the fields')
            else:
                st.session_state.user_name = st.session_state.login_email.split('@')[0]
                st.success(f'Successfully logged in as {st.session_state.user_name}')
                time.sleep(1)
                st.session_state.page='dashboard'
                st.rerun()

        if st.button(label='create account',use_container_width=True):
            st.session_state.page='Register'
            st.rerun()

elif st.session_state.page=='Register':
    st.title('create account')
    name=st.text_input('name',key='reg_name')
    email=st.text_input('email',key='reg_email',type='email')
    password=st.text_input('password',key='reg_password',type='password')

    if st.button('create',use_container_width=True):
        if not email or not password:
            st.warning('Please fill in all the fields')
        elif len(password)<5:
            st.error('Password is too short')
        elif len(name)<3:
            st.error('name is too short')
        else:
            st.success('Successfully created account')
            st.session_state.user_name=name
            st.session_state.page = 'dashboard'
            st.write(f'login {st.session_state.user_name}')
            time.sleep(3)
            st.rerun()
#         dashboard
elif st.session_state.page=='dashboard':

    st.title('Nexacore')
    st.write(f'welcome {st.session_state.user_name}')

    if 'message' not in st.session_state:
        st.session_state.message=[{'role':'assistant','content':f"hi  {st.session_state.user_name}  i'm your assistant "}]
    for msg in st.session_state.message:
        with st.chat_message(msg['role']):
            st.write(msg['content'])
    if prompt :=st.chat_input('ask me something'):
        st.session_state.message.append({'role':'user','content':prompt})
        with st.chat_message('user'):
            st.write(prompt)
        with st.chat_message('assistant'):
            with st.spinner('typing..'):
                time.sleep(1)
                reply=f'you said: {prompt}'
                st.write(reply)
                st.session_state.message.append({'role':'assistant','content':reply})


