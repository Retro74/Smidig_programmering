class Innlegg:
    def __init__(self, brukernavn:str, tekst:str, ant_likes:int=0):
        self.__brukernavn =  brukernavn
        self.__tekst =       tekst
        self.__ant_likes =   ant_likes
    def like_innlegg(self):
        self.__ant_likes +=1

    def vis_informasjon(self):
        return ", ".join(f"{innlegg_egenskap}={innlegg_egenskap_verdi}" for innlegg_egenskap, innlegg_egenskap_verdi in vars(self).items())


class BildeInnlegg(Innlegg):
    def __init__(self, brukernavn, tekst, ant_likes = 0, bilde_url:str="https://media.istockphoto.com/id/1222357475/vector/image-preview-icon-picture-placeholder-for-website-or-ui-ux-design-vector-illustration.jpg?s=612x612&w=0&k=20&c=KuCo-dRBYV7nz2gbk4J9w1WtTAgpTdznHu55W9FjimE="):
        super().__init__(brukernavn, tekst, ant_likes)
        self.bilde_url = bilde_url

class Videoinnlegg(Innlegg):
    def __init__(self, brukernavn, tekst, ant_likes = 0, video_lengde:int=0):
        super().__init__(brukernavn, tekst, ant_likes)
        self.video_lengde = video_lengde
    
bruker1_Innlegg1 = Innlegg("romi", "Hallaise", 10)
bruker1_Innlegg2 = Innlegg("romi", "Hallaise igjen", 21)
bruker1_BildeInnlegg1 = BildeInnlegg("romi", "Hallaise", 10, "http://anny.com/me.jpg")
bruker1_VidoeInnlegg1 = Videoinnlegg("romi", "Hallaise", 77, 666)

bruker1_Innlegg1.like_innlegg()
bruker1_Innlegg1.like_innlegg()
bruker1_VidoeInnlegg1.like_innlegg()
bruker1_VidoeInnlegg1.like_innlegg()

print(bruker1_Innlegg1.vis_informasjon())
print(bruker1_Innlegg2.vis_informasjon())
print(bruker1_BildeInnlegg1.vis_informasjon())
print(bruker1_VidoeInnlegg1.vis_informasjon())

