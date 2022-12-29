Http(Hypertext Transfer Protocol) é um protocolo de comunicação com um conjunto de regras. Funciona baseado na troca de requisição resposta, modelo servidor-cliente,

Http/1.1 trafega texto puro oque traz insegurança, não guarda estado entre conexões distintas

Dominio é um nome mais facil de ser gravado pelo humano cada dominio referencia um endereço ip do servdor. Dns

Ao acessar um recurso Url:<protocolo>://<servidor>:<porta>/<caminho>/<recurso>
exemplo > http://java.sun.com/docs/servlets/
A porta é um parametro que poder emitido, se for emitido a padrao sera utilizada, 40 para http e 443 para https

Para ter https é preciso certificvado digital e uma chave publica que apenas ela conhece, https é o protocolo http com uma camada a mais de segurança responsavel por criptografar os dados, uma entidade certificadora é responsavel por certificar essa criptografia

Alguns comandos HTTP: GET, POST, HEAD, PUT, DELETE
get solita ao servidor um recurso
post enviar dados para o servidor parametros das requisicoes vem no corpo


http2
envia header texto em binario + hpack
recebe heades texto em binario + hpack
corpo resposta em gzip 
criptografa com tls
cabecachos mantes estafdo no http/2
