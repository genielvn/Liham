import React from "react";
import style from "./Thread.module.scss";
import Link from "next/link";

interface ThreadProps {
    board: string;
}

const ThreadCreate: React.FC<ThreadProps> = ({ board }) => {
    return (
        <Link href={`/b/${board}/create`} style={{ textDecoration: "none" }}>
            <div className={style.thread}>
                <div className={style.thread__title}>
                    <i className="bi bi-plus-circle-fill margin-right-5" />
                    Start a New Thread
                </div>
            </div>
        </Link>
    );
};

export default ThreadCreate;
