from langserve import RemoteRunnable

if __name__ == "__main__":
    remote_chain = RemoteRunnable('http://localhost:8000/chain/')
    print(remote_chain.invoke({'language':'italian','text':'hello'}))