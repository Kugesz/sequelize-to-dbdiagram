import { Sequelize } from 'sequelize';
import sequelize from './database';
import Incomes from './model/Income';
import Inventory from './model/Inventory';
import Products from './model/Products';
import Tickets from './model/Tickets';
import Users from './model/Users';
import Workers from './model/Workers';

import ActiveWorkers from './model/runtime/ActiveWorkers';
import Tasks from './model/runtime/Tasks';

const initDB = async () => {
    try {
        await sequelize.authenticate();
        await sequelize.sync();
        console.log('Database synced!');
    } catch (error) {
        console.error('Unable to sync the database:', error);
    }
};

export default initDB;
