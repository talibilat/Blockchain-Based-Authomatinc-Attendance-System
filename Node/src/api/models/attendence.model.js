const mongoose = require('mongoose');

/**
 * Activity Schema
 * @private
 */
const AttendenceSchema = new mongoose.Schema({
    hash: { type: String },                        //1 = login, 2 = add, 3 = edit, 4 = delete, 5 = search
    documnetName: { type: String },            //game,tournament,staff,faqs,rewards,news,learning
}, { timestamps: true }
);



/**
 * @typedef Attendence
 */

module.exports = mongoose.model('Attendence', AttendenceSchema);