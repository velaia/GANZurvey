import sys
import site
site.addsitedir('/home/velaia/.virtualenvs/GANZurveyEnv/lib/python3.6/')
sys.path.insert(0, '/home/velaia/git/GANZurvey')
sys.stdout = sys.stderr
from app import app as application