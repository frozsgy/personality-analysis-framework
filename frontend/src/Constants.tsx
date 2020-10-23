export const server = "https://www.tweetkisiligim.xyz/api/"; //;"http://localhost:8080/";//
export const frontend = "https://www.tweetkisiligim.xyz/";

export const getKey = (key = "name") => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  return urlParams.get(key);
};

export const openTwitter = () => {
  const url = "https://twitter.com/TweetKisiligim";
  window.open(url);
};

export const labelsBigFive = [
  "Açıklık",
  "Sorumluluk",
  "Dışadönüklük",
  "Uyumluluk",
  "Nevrotiklik",
];

export const describeBigFive = [
  "Açıklık (openness), kişilerin yeni şeyler denemeye, entelektüel ve hayalperest aktivitelere katılmaya olan isteklerini temsil eder. Açıklık skoru yüksek olan insanlar daha meraklı iken, düşük çıkan insanlar değişiklikten hoşlanmayan bir yapıdadır.",
  "Sorumluluk (conscientiousness), bir insanın anlık dürtülerini kontrol edebilme yetisini ifade eder. Kontrollülük, davranışlarda kalıcılık gibi elementleri kapsar. Sorumluluk skoru yüksek çıkan insanlar daha organize, düşünceli ve dikkatli olma eğilimindedirler. Düşük çıkan insanlar ise düzensiz olabilir ve yapılanmaktan hoşlanmayabilirler.",
  "Dışadönüklük (extraversion), insanların sosyal çevreleriyle etkileşimde bulunma eğilim ve sıklıklarını ifade eder. Dışadönüklük skoru yüksek olan insanlar sosyal durumlarda daha rahat ve kararlı davranırlar.",
  "Uyumluluk (agreeableness), kişinin diğer insanlarla olan ilişkilerinizde nasıl davrandığını gösterir. Uyumluluk skoru yüksek olan insanlar daha açık sözlü ve alçakgönüllü olurken, düşük çıkan insanlar başkalarına daha şüpheci ve talepkar yaklaşır.",
  "Nevrotiklik (neuroticism), bireylerin genel olarak duygusal kararlılığını dünyayı idrak etme şekilleri üzerinden açıklar. Bir kişinin karşılaştığı olayları tehditkar ya da zorlayıcı olarak yorumlama ihtimallerini göz önünde bulundurur. Nevrotiklik skoru yüksek çıkan insanlar daha endişeli ve stresli olabilir.",
];
