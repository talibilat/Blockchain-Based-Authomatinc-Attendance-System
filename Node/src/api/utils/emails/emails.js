const Settings = require('../../models/settings.model')
const Mail = require('../../models/email.model')
const {emailAdd,mailgunDomain,mailgunApi} = require('../../../config/vars')

//send email to mentioned users
exports.sendEmail = async (email = '', type = '', content = null, subject = '') => {
    try {
        if (email !== '') {
            const getTemplate = await Mail.findOne({ type })
            if (getTemplate) {
                let setting = await Settings.findOne()
                let api=setting?.api ? setting?.api : '';
                let domain=setting?.domain ? setting?.domain : '';
                if(!api && !domain) {
                    api=mailgunApi
                    domain=mailgunDomain
                }
                console.log(api,domain)
                var mailgun = require('mailgun-js')({ apiKey: api, domain: domain });
                let sub = ''
                if(subject) {
                    sub = subject
                }
                else {
                    sub = getTemplate.subject
                }
                const msg = {
                    to: email,
                    from: emailAdd,
                    subject: sub,
                    html: getHtml(getTemplate, content)
                };


    
                mailgun.messages().send(msg, function (err,body) {
                    if (err) {
                        console.log('err',err)
                    }
                    else {
                        console.log(body)
                    }
                });
            }
        }
    }
    catch (e) {
        console.log(e)
    }
}

function getHtml(getTemplate, content) {
    let text = getTemplate.text
    if (content) {
        for (let key in content) {
            text = text.replace(`${key}`, "'" + `${content[key]}` + "'")
        }
    }
    return text
}