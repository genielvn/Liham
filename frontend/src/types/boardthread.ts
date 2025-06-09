import { BoardData } from "./board";
import { ThreadData } from "./thread";

export interface BoardThreadListData {
    board: BoardData;
    threads: ThreadData[];
}

export interface SingleBoardThreadData { 
    board: BoardData;
    thread: ThreadData;
}
