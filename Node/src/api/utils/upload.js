// multer
const fs = require('fs')
const multer = require('multer')
const cloudinary = require('cloudinary')
const { resolve } = require('path')
const uploadsDir = './src/uploads/'
const imagesDir = `${uploadsDir}images`
cloudinary.config({
    cloud_name: process.env.CLOUD_NAME,
    api_key: process.env.API_KEY,
    api_secret: process.env.API_SECRET
});

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        // make uploads directory if do not exist
        if (!fs.existsSync(uploadsDir))
            fs.mkdirSync(uploadsDir)

        if (!fs.existsSync(imagesDir))
            fs.mkdirSync(imagesDir)

        cb(null, imagesDir)
    },
    filename: function (req, file, cb) {
        var fileExtension = file.mimetype.split("/")[1]
        if (!file.originalname.toLowerCase().match(/\.(jpg|jpeg|png|gif|svg|apk|csv|xls|xlsx|ipa)$/)) {
            return cb(new Error('Only image files are allowed.'))
        }
        cb(null, + Date.now() + '.' + fileExtension)
    }
})      

const upload = multer({ storage })
exports.cpUpload = upload.fields([{ name: 'image', maxCount: 1 },{ name: 'thumbnail', maxCount: 1 },{ name: 'screenShot', maxCount: 1 },{ name: 'icon', maxCount: 1 },{ name: 'files', maxCount: 1 },{ name: 'manifestFile', maxCount: 1 },{ name: 'crashLog', maxCount: 1 },{ name: 'profileImage', maxCount: 1 },{ name: 'avatar', maxCount: 1 },{ name: 'userImage', maxCount: 1 },{name: 'tutorialImage' , maxCount: 1},{name: 'backgroundImage' , maxCount: 1},{name: 'icon' , maxCount: 1}  ])
exports.uploadSingle = upload.single('image')
exports.uploadContentImage = upload.single('files')
exports.profileUpload = upload.fields([{ name: 'profileImage', maxCount: 1 }, { name: 'bannerImage', maxCount: 1 }])


exports.uploadToCloudinary = async (data) => {

    return new Promise((resolve)=>{
        cloudinary.uploader.upload(data,(result)=>{
            console.log("result",result)
            resolve(result.secure_url)},{resource_type:"auto"} );
    })

    // return `oooooooooooo`
}

