import pystache
import json 
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--config", dest="configFile",
                  help="load the config from the FILE", metavar="FILE")
                  
parser.add_option("-t", "--template", dest="templateFile",
                  help="load the template from the FILE", metavar="FILE")
                  
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()


json_file = open(options.configFile)
data = json.load(json_file)
json_file.close()


template_file = open(options.templateFile)
template = template_file.read()

print pystache.render(template, data)

