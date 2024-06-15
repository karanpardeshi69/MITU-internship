class batsman:
    def findaverage(runs, outs):
        if outs == 0:
            return 0
        return runs / outs

    def strikerate(runs, balls):
        if balls == 0:
            return 0
        return (runs / balls) * 100
class bowler:
    def findavg(runs, wickets):
      if wickets == 0:
          return 0
      return runs / wickets

    def economyrate(overs, runs):
      if overs == 0:
         return 0
      return runs / overs
