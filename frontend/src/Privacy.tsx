import React from "react";
import {
  Container,
  Grid,
  Header,
  Segment,
  List,
} from "semantic-ui-react";
import BottomMenu from "./Menu";
import { contactDetails } from "./Contact";

const Privacy = () => {
  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header size="large">Gizlilik Bildirimi</Header>
                <p>
                  Projemiz kapsamında kişisel verilerin gizliliği konusunu çok
                  ciddiye alıyoruz ve kullanıcılarımızı verilerini nasıl
                  kullandığımız hakkında bilgilendirmek istiyoruz. Aşağıda
                  verilerin kullanılması ve saklanması hakkında gerekli
                  bilgileri bulabilirsiniz.{" "}
                </p>
                <Header size="large">Veri Saklama</Header>
                <Header size="medium">Kişisel Veriler</Header>
                <p>
                  Tweet Kişiliğim uygulamasına giriş yaptığınızda,
                  servislerimizi kullanabilmeniz için Twitter hesabınızla dair
                  bazı verilere erişiyoruz. Bunlar;
                </p>
                <List bulleted>
                  <List.Item>Size özgü Twitter ID’niz</List.Item>
                  <List.Item>Kullanıcı adınız (@)</List.Item>
                </List>
                <p>
                  Eğer uygulamamızı kullanmaktan vazgeçerseniz, veri
                  izinlerinizi{" "}
                  <a
                    href="https://twitter.com/settings/applications"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    https://twitter.com/settings/applications
                  </a>{" "}
                  adresinden kaldırabilirsiniz.
                </p>

                <Header size="medium">Sonuçlar</Header>
                <p>
                  Tweet Kişiliğim ile elde ettiğiniz kişilik profili
                  sistemimizde bilimsel çalışmalarda kullanılmak üzere
                  kaydedilmektedir. Ancak elde ettiğiniz sonuç, siz
                  istemediğiniz sürece hiçbir yerle paylaşılmamaktadır.{" "}
                </p>
                <p>
                  Anket çalışmamıza katılmak istediğiniz takdirde, ankete
                  verdiğiniz cevaplar, sonuçlarınız ile eşleştirilmektedir.
                  Anket çalışmasına katılmak tamamen gönüllülük esasına
                  dayanmaktadır.
                </p>
                <Header size="large">Veri İşleme</Header>

                <p>
                  Uygulamamızı kullanırken Twitter hesabınızdan atılmış son 3200
                  tweet’i toplayıp işlemekteyiz. Veri işleme süreci sistem
                  yoğunluğuna göre değişmekle birlikte 10 dakikayı
                  geçmemektedir. Bu sürecin sonunda topladığımız tweet’lerinizi
                  doğal dil işleme yöntemleri ile sayısal değerlere
                  dönüştürmekteyiz. Bu sayısal verilerden tekrar sizin
                  tweetlerinizin elde edilebilmesi mümkün değildir.{" "}
                </p>

                <Header size="large">Paylaşma</Header>
                <p>
                  Tweet Kişiliğim’e giriş yaptığınız zaman, hesabınız üzerinde
                  temel okuma ve yazma izinleri istiyoruz. Sizin isteğiniz
                  dışında herhangi bir paylaşımda bulunmuyoruz. Eğer
                  uygulamamızı kullanmaktan vazgeçerseniz, veri izinlerinizi{" "}
                  <a
                    href="https://twitter.com/settings/applications"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    https://twitter.com/settings/applications
                  </a>{" "}
                  adresinden kaldırabilirsiniz.
                </p>
                <Header size="large">Sorularınız için:</Header>
                {contactDetails}
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Privacy;
