import os
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
api_wrapper = WolframAlphaAPIWrapper(wolfram_alpha_appid=os.environ['WOLFRAM_ALPHA_APPID'])
print(api_wrapper.run("What is 2x+5 = -3x + 7?"))
