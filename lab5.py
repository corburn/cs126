import time

updates = []

# status - the text of a status update. Example: "Storming the village at 9. Anyone interested?"
# audience - a list of audiences that may be interested. Example: ["Zombies", "Vampires"]
# userid - the handle of the person posting the update. Example: "BarnabasCollins"
# time - the time of the tweet using unix epoch
# id - the id of the post
def update(status, audience, userid, time):
	updates.append({'status': status, 'audience': audience, 'userid': userid, 'time': time, 'likes': set()})
	return len(updates)-1

# id - the id of the post to like
# userid - the handle of the person posting the update. Example: "BarnabasCollins"
def like(id, userid):
	updates[id]['likes'].add(userid)

# id - the id of the post to like
# userid - the handle of the person posting the update. Example: "BarnabasCollins"
def unlike(id, userid):
	updates[id]['likes'].discard(userid)

# userid - the handle of the person whose updates should be displayed. Example: "BarnabasCollins"
def display(userid):
	for u in updates:
		if(u['userid'] == userid):
			print "Time: " + str(u['time'])
			print "Groups: " + ', '.join(u['audience'])
			print "Likes: " + str(len(u['likes']))
			print userid + " (mention with @" + userid + ") says:"
			print u['status'] + '\n'

p = update("Storming the village at 9.  Anyone interested?",
           ["Zombies", "Vampires"],
           "BarnabasCollins",
           1349708829)

q = update("Can I come?",
           ["Vampires"],
           "Casper",
           1349708835)

r = update("Forgot to include the ghosts! LOL",
           ["Ghosts"],
           "BarnabasCollins",
           1349708845)

s = update("Lots of villagers with forks here..",
           ["Vampires", "Zombies", "Ghosts"],
           "BarnabasCollins",
           1349708900)

like(p, "Edmund")
like(p, "Grimm")
like(p, "Edmund")
like(q, "Edmund")
like(q, "Grimm")
like(q, "Harry")
like(r, "Casper")
like(s, "Casper")

display("BarnabasCollins")
print "---"
display("Casper")
