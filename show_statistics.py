import logging
from pyhelpers import tools, grobid_mapping
import config
tools.setup_logging()
import pprint
import json


def main(filter:("filter","option")=None):
    """

    :param filter: -filter="{'printConf' : 'yes', 'printJournal' : 'yes', 'printColl': 'yes', 'showPdfProg' :'yes', 'showExtractedSents':'yes'}"
    :return:
    """


    filters = json.loads(filter.replace("'", '"'))
    if filter:
        filters = json.loads(filter.replace("'", '"'))
        print("Using filters " + str(filters))
    print(filters)
    db = tools.connect_to_mongo()
    if len(filters) > 0:
        for k, v in filters.items():
            if k == "showPdfProg" and v == "yes":

                result = db.downloads.count({"success" : True})
                print('{:>25} {:>8d}'.format("PDFs downloaded", result))
                #
                result = db.downloads.count({"success": False})
                print('{:>25} {:>8d}'.format("broken DBLP links", result))
                #
                result = db.publications.count({"content": {"$exists": True}})
                print('{:>25} {:>8d}'.format("fulltexts extracted", result))

                #print the papers from WWW
                result = db.publications.count({"booktitle": "WWW"})
                print('{:>25} {:>8d}'.format("WWW papers", result))

                result = db.publications.count({'$and' : [{'booktitle' :'WWW'} , {'content.chapters':{'$exists':True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions WWW papers", result))

                #'JCDL,SIGIR,ECDL,TPDL,TREC'
                #Print JCDL papers
                result = db.publications.count({"booktitle": "JCDL"})
                print('{:>25} {:>8d}'.format("JCDL papers", result))

                result = db.publications.count(
                    {'$and': [{'booktitle': 'JCDL'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions JCDL papers", result))

                # Print ECDL papers
                result = db.publications.count({"booktitle": "ECDL"})
                print('{:>25} {:>8d}'.format("ECDL papers", result))

                result = db.publications.count(
                    {'$and': [{'booktitle': 'ECDL'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions ECDL papers", result))

                # Print TPDL papers
                result = db.publications.count({"booktitle": "TPDL"})
                print('{:>25} {:>8d}'.format("TPDL papers", result))

                result = db.publications.count(
                    {'$and': [{'booktitle': 'TPDL'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions TPDL papers", result))

                # Print TREC papers
                result = db.publications.count({"booktitle": "TREC"})
                print('{:>25} {:>8d}'.format("TREC papers", result))

                result = db.publications.count(
                    {'$and': [{'booktitle': 'TREC'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions TREC papers", result))

                # Print ICSE papers
                result = db.publications.count({"booktitle": "ICSE"})
                print('{:>25} {:>8d}'.format("ICSE papers", result))

                result = db.publications.count(
                    {'$and': [{'booktitle': 'ICSE'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions ICSE papers", result))

                #print the papers from SIGIR
                result = db.publications.count({"booktitle": "SIGIR"})
                print('{:>25} {:>8d}'.format("SIGIR papers", result))

                result = db.publications.count({'$and' : [{'booktitle' :'SIGIR'} , {'content.chapters':{'$exists':True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions SIGIR papers", result))


                #print the papers from ESWC
                result = db.publications.count({"booktitle": "ESWC"})
                print('{:>25} {:>8d}'.format("ESWC papers", result))

                #result = db.publications.find_one({"dblpkey":"conf_esws_BruggemannBXK16"})
                #print(result)
                #if result is None:
                #    print("No entry")


                result = db.publications.count({'$and' : [{'booktitle' :'ESWC'} , {'content.chapters':{'$exists':True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions ESWC papers", result))

                #print the papers from ICWSM
                result = db.publications.count({"booktitle": "ICWSM"})
                print('{:>25} {:>8d}'.format("ICWSM papers", result))

                result = db.publications.count({'$and' : [{'booktitle' :'ICWSM'} , {'content.chapters':{'$exists':True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions ICWSM papers", result))


                #print the papers from VLDB
                result = db.publications.count({"booktitle": "VLDB"})
                print('{:>25} {:>8d}'.format("VLDB papers", result))

                result = db.publications.count({'$and' : [{'booktitle' :'VLDB'} , {'content.chapters':{'$exists':True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions VLDB papers", result))

                # print the papers from SOCROB
                result = db.publications.count({"booktitle": "ICSR"})
                print('{:>25} {:>8d}'.format("ICSR papers", result))

                result = db.publications.count(
                  {'$and': [{'booktitle': 'ICSR'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions ICSR papers", result))

                # print the papers from HRI
                result = db.publications.count({"booktitle": "HRI"})
                print('{:>25} {:>8d}'.format("HRI papers", result))

                result = db.publications.count(
                  {'$and': [{'booktitle': 'HRI'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions HRI papers", result))

                # print the papers from TROB
                result = db.publications.count({"journal": "TROB"})
                print('{:>25} {:>8d}'.format("TROB papers", result))

                result = db.publications.count(
                  {'$and': [{'journal': 'TROB'}, {'content.chapters': {'$exists': True}}]})
                print('{:>25} {:>8d}'.format("Successful extractions TROB papers", result))


            if k == "printColl" and v == "yes":
                print("Collections in MongoDB")
                collections = db.collection_names()
                for collection in collections:
                    print(collection)
                print()

            if k == "showExtractedSents" and v == "yes":
                sentences = db.sentences.find({}).count()
                print("Extracted Sentences: {}".format(sentences))

                sentences = db.sentences.find({"objective": 1}).count()
                print("Extracted Sentences objective: {}".format(sentences))

                sentences = db.sentences.find({"method": 1}).count()
                print("Extracted Sentences method: {}".format(sentences))

                sentences = db.sentences.find({"software": 1}).count()
                print("Extracted Sentences software: {}".format(sentences))

                sentences = db.sentences.find({"dataset": 1}).count()
                print("Extracted Sentences dataset: {}".format(sentences))

                sentences = db.sentences.find({"result": 1}).count()
                print("Extracted Sentences result: {}".format(sentences))

                sentences = db.sentences.find({"other": 1}).count()
                print("Extracted Sentences other: {}".format(sentences))


                print()
            if k == "printConf" and v == "yes":
                result = db.publications.distinct("booktitle")
                # print("Booktitles")
                f = open(config.folder_log + "booktitles_summary.csv", "w", encoding="UTF-8")
                f.write("Conferences,#Papers,#Extracted,#Not Extracted")
                f.write("\n")
                for r in result:
                    count_booktitle = db.publications.find({"booktitle": r}).count()
                    count_extracted = db.publications.find({'$and': [{'booktitle': r}, {'content.chapters': {'$exists': True}}]}).count()
                    count_not_extracted = db.publications.find(
                        {'$and': [{'booktitle': r}, {'content.chapters': {'$exists': False}}]}).count()
                    f.write("{},{},{},{}".format(str(r).replace(",",""), count_booktitle,count_extracted,count_not_extracted))
                    f.write("\n")
                    # print("{}: {}".format(r, count_booktitle))
                f.close()

            if k == "printJournal" and v == "yes":
                result = db.publications.distinct("journal")
                # print("Journals")
                f = open(config.folder_log + "journal_summary.csv", "w", encoding="UTF-8")
                for r in result:
                    count_journal = db.publications.find({"journal": r}).count()
                    f.write("{},{}".format(r, count_journal))
                    f.write("\n")
                    # print("{}: {}".format(r,count_journal))
                f.close()
    else:
        print("Use filters e.g.  -filter=\"{'printConf' : 'yes', 'printJournal' : 'yes', 'printColl': 'yes', 'showPdfProg' :'yes', 'showExtractedSents}")
    """
    result = db.publications.distinct("journal")
    #print("Journals")
    f = open(config.folder_log+"journal_summary.csv", "w", encoding="UTF-8")
    for r in result:
        count_journal = db.publications.find({"journal": r}).count()
        f.write("{},{}".format(r,count_journal))
        f.write("\n")
        #print("{}: {}".format(r,count_journal))
    f.close()


    result = db.publications.distinct("booktitle")
    #print("Booktitles")
    f = open(config.folder_log+"booktitles_summary.csv", "w", encoding="UTF-8")
    for r in result:
        count_booktitle = db.publications.find({"booktitle": r}).count()
        f.write("{},{}".format(r, count_booktitle))
        f.write("\n")
        #print("{}: {}".format(r, count_booktitle))
    f.close()
    """

if __name__ == '__main__':
    import plac
    plac.call(main)
