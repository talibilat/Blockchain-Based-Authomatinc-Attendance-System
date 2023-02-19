const express = require('express');
const controller = require('../../../controllers/main/attendence.controller');
const router = express.Router();
const { profileUpload,uploadSingle } = require('../../../utils/upload')

router.route('/').post(controller.init1);
router.route('/upload-image').post(uploadSingle,controller.uploadFile);


module.exports = router;