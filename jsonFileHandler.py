{
   "molecules":{
      "lsInsulin":"malwmrllpllallalwgpdpaaa",
      "bInsulin":"fvnqhlcgshlvealylvcgergffytpkt",
      "aInsulin":"giveqcctsicslyqlenycn",
      "cInsulin":"rreaedlqvgqvelgggpgagslqplalegslqkr"
   },
   "weights":{
      "A":89.09,
      "C":121.16,
      "D":133.10,
      "E":147.13,
      "F":165.19,
      "G":75.07,
      "H":155.16,
      "I":131.17,
      "K":146.19,
      "L":131.17,
      "M":149.21,
      "N":132.12,
      "P":115.13,
      "Q":146.15,
      "R":174.20,
      "S":105.09,
      "T":119.12,
      "V":117.15,
      "W":204.23,
      "Y":181.19
   },
   "molecularWeightInsulinActual":5807.63
}
import json
def readJsonFile(fileName):
  data=""         
  def readJsonFile(fileName):
    data = ""
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data