s = '''
Of course Docker is still here, and of course everyone is still using Docker and will continue to do so the near and foreseeable future (how far that foreseeable future is - is yet to be determined). The reason I chose this title for the blogpost is because, in my humble opinion the days for Docker as a company are numbered and maybe also a technology as well. If would indulge me with a few minutes of your time - I will share with you the basis for my thoughts.
A number of years ago - Docker was the company that changed the world - and we can safely say - is still changing the world today. Containers and the technology behind containers has been around for many years, long before the word docker was even thought of, even turned into a verb (“Dockerize all the things”), but Docker was the company that enabled the masses to consume the technology of containers, in a easy and simple fashion. Most technology companies (or at least companies that consider themselves to be a modern tech company) will be using Docker or containers as part of their product or their pipeline - because it makes so much sense and brings so much benefit to whole process.
Over the past 12-24 months, people are coming to the realization that docker has run its course and as a technology is not going to be able to provide additional value to what they have today - and have decided to start to look elsewhere for that extra edge.
Kubernetes has won the container orchestration war, I don’t think that anyone can deny that fact. Docker itself has adopted Kubernetes. There will always be niche players that have specific use cases for Docker Swarm, Mesos, Marathon, Nomad - but the de-facto standard is Kubernetes. All 3 big cloud providers, now have a managed Kubernetes solution that they offer to their customers (and as a result will eventually sunset their own home-made solutions that they built over the years - because there can be only one). Everyone is building more services and providing more solutions, to bring in more customers, increase their revenue.
Story is done. Nothing to see here. Next shiny thing please..
At the moment, Kubernetes uses docker as the underlying container engine. I think that the Kubernetes community understood that Docker as a container runtime (and I use this term specifically) was the ultimate solution to get a product out of the gate as soon as possible. They also (wisely) understood quite early on they needed to have the option of switching out that container runtime - and allowing the consumers of Kubernetes to make a choice.
The Open Container Initiative - brought with it the Runtime Spec - which opened the door to allow us all to use something else besides docker as the runtime. And they are growing - steadily. Docker is no longer the only runtime that is being used. Their is a growth in the community - that are slowly sharing the knowledge of how use something else besides Docker. Kelsey Hightower - has updated his Kubernetes the hard way (amazing work - honestly) over the years from CRI-O to containerd to gvisor. All the cool kids on the block are no longer using docker as the underlying runtime. There are many other options out there today clearcontainers, katacontainers and the list is continuously growing.
Most people (including myself) do not have enough knowledge and expertise of how to swap out the runtime to what ever they would like and usually just go with the default out of the box. When people understand that they can easily make the choice to swap out the container runtime, and the knowledge is out there and easily and readily available, I do not think there is any reason for us to user docker any more and therefore Docker as a technology and as a company will slowly vanish. The other container runtimes that are coming out will be faster, more secure, smarter, feature rich (some of them already are) compared to what Docker has to offer. If you have a better, smarter, more secure product - why would people continue to use technology that no longer suits their ever increasing needs?
For Docker - to avert this outcome - I would advise to invest as much energy as possible - into creating the best of breed runtime for any workload - so that docker remains the de-facto standard that everyone uses. The problem with this statement - is that there no money in a container runtime. Docker never made money on their runtime, they looked for their revenue on the enterprise features above and on top the container runtime. How they are going to solve this problem - is beyond me and the scope of this post.
The docker community has been steadily declining, the popularity of the events has been declining, the number of new features, announcements - is on the decline and has been on the decline for the past year or two.
Someone told me a while back - that speaking bad about things or giving bad news is usually very easy. We can easily say that this is wrong, this is no useful, this should change. But without providing a positive twist on something - you become the “doom and gloom”. The “grim reaper”. Don’t be that person.
I would like to heed their advice, and with that add something about - what that means for you today. You should start investing in understanding how these other runtimes can help you, where they fit, increase your knowledge and expertise - so that you can prepare for this and not be surprised when everyone else stops using docker and you find yourself having to rush into adapting all your infrastructure. I think it is inevitable.

'''
def max_freq_word(text):
    freqs = {}
    top_word = 'tempval'
    freqs[top_word] = 0
    text_list = text.lower().split()
    for word in text_list:
        if word in freqs:
            freqs[word] +=1
        else:
            freqs[word] = 1
        if freqs[word] > freqs[top_word]:
            top_word = word
    return top_word, freqs[top_word]

print (s.split())
print (max_freq_word(s))

