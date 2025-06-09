import { UserData } from "./user";
import { ThreadData } from "./thread";
import { ReplyData } from "./reply";

export interface UserBoardThreadData {
    user: UserData;
    threads: ThreadData[];
    replies: ReplyData[];
}
