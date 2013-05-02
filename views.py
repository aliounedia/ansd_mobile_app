from django.shortcuts import render_to_response
import json
json_dir   = "."

def search(request, template_name):
    """simple list"""
    list = []
    for package in json.load(
        open(json_dir + "\\ansd_dataset_search_tojson.json", "rb")):
        print "package", package 
        list.append(package )
    return render_to_response(template_name,
                        {"packages" :list})
        
def group_seach(request, template_name):
    """list with category"""
    list   = []
    groups = {'ihpc': {"counts" : 0, "elements" :[]},
             'inpc': {"counts" : 0, "elements" :[]}}
    for package in json.load(
        open(json_dir + "\\ansd_dataset_search_tojson.json", "rb")):
        if "ihcp" in package:
            groups["ihcp"]["counts"] = groups["ihcp"]["counts"] + 1
            groups["ihcp"]["elements"].append(package)
        elif "inpc" in package:
            groups["inpc"]["counts"] = groups["inpc"]["counts"] + 1
            groups["inpc"]["elements"].append(package)  
    return render_to_response(template_name,
                        {"packages" :groups})
def info(request):
    pass

def alter(request):
    pass
