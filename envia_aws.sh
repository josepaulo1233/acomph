ano=$(date +%Y)
echo $ano
mes=$(date +%m)
echo $mes
dia=$(date +%d)
echo $dia
#dia=01
aws s3 cp grande/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/grande/ --recursive
aws s3 cp paranaiba/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/paranaiba/ --recursive
aws s3 cp tocantins/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/tocantins/ --recursive
aws s3 cp iguacu/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/iguacu/ --recursive
aws s3 cp saofrancisco/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/saofrancisco/ --recursive
aws s3 cp parana/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/parana/ --recursive
aws s3 cp paranapanema/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/paranapanema/ --recursive
aws s3 cp uruguai/ s3://conmet-website/media/predictions/${ano}-${mes}-${dia}/psat_ons/-/ena-prec/uruguai/ --recursive
