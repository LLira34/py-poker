from distutils.core import setup 
import py2exe 
 
setup(name="Poker", 
 version="1.0", 
 description="Juego de Poker con Python y pygame", 
 author="autor", 
 author_email="email del autor", 
 url="url del proyecto", 
 license="tipo de licencia", 
 scripts=["PokerGame.py"], 
 console=["PokerGame.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)