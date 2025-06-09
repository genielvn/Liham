import style from "./ThreadReplyTab.module.scss";
import { useState } from "react";
import UserThread from "./UserThread";
import UserReply from "./UserReply";
import { UserBoardThreadData } from "@/types/userboardthread";

interface ThreadReplyTabProps {
    data: UserBoardThreadData | null;
}
export default function ThreadReplyTab({ data }: ThreadReplyTabProps) {
    const [activeTab, setActiveTab] = useState<"threads" | "replies">(
        "threads"
    );

    return (
        <div className={style.thread_reply__main}>
            <div className={style.thread_reply__toggleSwitch}>
                <button
                    className={`btn-small-no-min ${
                        activeTab === "threads"
                            ? "btn-solid-pink"
                            : "btn-hollow-pink"
                    }`}
                    onClick={() => setActiveTab("threads")}
                >
                    Threads
                </button>
                <button
                    className={`btn-small-no-min ${
                        activeTab === "replies"
                            ? "btn-solid-pink"
                            : "btn-hollow-pink"
                    }`}
                    onClick={() => setActiveTab("replies")}
                >
                    Replies
                </button>
            </div>

            {activeTab === "threads" && (
                <div>
                    {data?.threads.length === 0 && <p>No threads found.</p>}
                    {data?.threads.map((reply, index) => (
                        <UserThread
                            key={index}
                            id={reply.id}
                            board={reply.board}
                            title={reply.title}
                            text={reply.body}
                            img_upload={reply.img_upload}
                            created_at={reply.created_at}
                        />
                    ))}
                </div>
            )}

            {activeTab === "replies" && (
                <div>
                    {data?.replies.length === 0 && <p>No replies found.</p>}
                    {data?.replies.map((reply, index) => (
                        <UserReply
                            key={index}
                            thread_title={reply.thread_title}
                            content={reply.body}
                            img_upload={reply.img_upload}
                            created_at={reply.created_at}
                            board={reply.board}
                            thread={reply.thread}
                        />
                    ))}
                </div>
            )}
        </div>
    );
}
